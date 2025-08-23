# 🤖 AI Blog Writer Setup

This workflow automatically generates and publishes blog posts to Dev.to using Google's Gemini AI.

## 🔧 Setup Instructions

### 1. Required API Keys

You need to add these secrets to your GitHub repository:

#### **GEMINI_API_KEY**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

#### **DEVTO_API_KEY**
1. Go to [Dev.to Settings](https://dev.to/settings/extensions)
2. Generate a new API key
3. Copy the key

### 2. Add Secrets to GitHub

1. Go to your repository settings
2. Navigate to **Secrets and variables** → **Actions**
3. Add these repository secrets:
   - `GEMINI_API_KEY`: Your Google AI API key
   - `DEVTO_API_KEY`: Your Dev.to API key

## 🎯 How It Works

### Automatic Posting
- **Schedule**: Every Monday at 3:30 PM IST
- **Content**: AI generates based on your GitHub activity
- **Topics**: Rotates between tutorials, project showcases, tech insights

### Manual Triggering
1. Go to **Actions** tab in your repository
2. Select **🤖 AI Auto Blog Writer**
3. Click **Run workflow**
4. Choose:
   - **Post Type**: tutorial, project-showcase, tech-insights, career-tips, ai-ml-trends
   - **Topic** (optional): Specific topic to write about

## 📝 Post Types

### 1. **Tutorial** 
- Step-by-step technical guides
- Code examples and best practices
- Beginner-friendly explanations

### 2. **Project Showcase**
- Your latest GitHub projects
- Technical architecture details
- Problem-solving approaches

### 3. **Tech Insights**
- Industry trends and analysis
- Expert opinions on emerging tech
- Future predictions

### 4. **Career Tips**
- Personal career journey insights
- Advice for developers
- Growth strategies

### 5. **AI/ML Trends**
- Latest AI/ML developments
- Practical applications
- Implementation insights

## 🎨 Content Features

### AI-Generated Content Includes:
- ✅ **Engaging titles and hooks**
- ✅ **Technical accuracy** based on your expertise
- ✅ **Code examples** and practical tips
- ✅ **Proper Dev.to formatting**
- ✅ **Relevant hashtags**
- ✅ **SEO-optimized content**

### Content Sources:
- 📊 **Your GitHub activity** (commits, repos, languages)
- 🏆 **Your achievements** (IEEE papers, grants, awards)
- 💼 **Your experience** (AI/ML, Full-Stack, Research)
- 🎯 **Current tech trends**

## 📊 Monitoring

### Check Results:
1. **GitHub Actions**: View workflow runs and logs
2. **Generated Files**: `.md` files saved in repository
3. **Dev.to Profile**: Published articles appear automatically
4. **Workflow Summary**: Detailed results after each run

### Success Indicators:
- ✅ Green workflow status
- 📝 New `.md` file in repository
- 🔗 Article URL in workflow summary
- 📱 New post on your Dev.to profile

## 🛠️ Customization

### Modify Content Style:
Edit the prompts in `ai-blog-writer.yml` to change:
- Writing tone and style
- Content structure
- Technical depth
- Target audience

### Adjust Scheduling:
Change the cron expression in the workflow:
```yaml
schedule:
  - cron: '0 10 * * 1'  # Every Monday at 10 AM UTC
```

### Add More Post Types:
Extend the `prompts` dictionary with new content types and templates.

## 🚨 Safety Features

- **Content Review**: Generated content is saved locally before publishing
- **Error Handling**: Comprehensive error catching and logging
- **Rate Limiting**: Respects Dev.to API rate limits
- **Quality Control**: AI generates high-quality, relevant content

## 📈 Benefits

- 🤖 **Consistent Content**: Regular blog posts without manual effort
- 🎯 **Personalized**: Content based on YOUR projects and expertise
- 📱 **Auto-Publishing**: Direct publication to Dev.to
- 📊 **SEO Optimized**: AI creates search-friendly content
- 🎨 **Professional Quality**: Well-structured, engaging articles

---

*Ready to start? Add the API keys and let AI handle your blogging! 🚀*
